#!/usr/bin/env perl

use 5.010;

use YAML;
use Cwd qw/abs_path/;
use File::Basename qw/dirname basename/;
use File::Spec::Functions qw/catfile/;

use Data::Dumper;
# use Data::Dump qw/dump/;

my $__file__ = basename __FILE__;

my $apps = [
    "/home/lane/Mmrz-Sync/server/Mmrz-Sync.py",
    "/home/lane/wx-globe/wx-globe.py",
    "/home/lane/navi-site/navi-site.py",
    "/home/lane/lhsjlc4/lhsjlc4.rb",
    "/home/lane/tools-lite/ruby/bingAPI.rb",
    "/home/lane/tools-lite/ruby/returnAddr.rb",
];

my $g_applist_yaml = "applist.yml";

sub load_yaml_config {
    open my $fr, "<", $g_applist_yaml;
    my @content = <$fr>;
    close $fr;

    my $app_list = YAML::Load join("", @content);
    return $app_list;
}

sub dump_yaml_config {
    my $app_list = shift;

    my $yml_string = YAML::Dump $app_list;
    open my $fw, ">", $g_applist_yaml;
    print $fw $yml_string;
    close $fw;
}

sub grep_app_name {
    my $name = shift;

    my @pids = `ps -ef | grep -v grep | grep $name | awk '{print \$2}'`;

    my @details;
    for my $pid (@pids) {
        chomp($pid);

        my $cwd = readlink "/proc/$pid/cwd";
        next unless defined $cwd;

        my $exe = readlink "/proc/$pid/exe";
        next unless defined $exe;

        my $cmdline = `cat /proc/$pid/cmdline`;
        my @cmdline_arr = split /\0/, $cmdline;
        my $app_name = $cmdline_arr[1];
        my $full_path = abs_path catfile($cwd, $app_name);

        my $detail = {
            pid => $pid,
            exe => $exe,
            cwd => $cwd,
            app => $app_name,
            full_path => $full_path,
        };

        push @details, $detail;
    }

    return \@details;
}

sub active_or_down {
    my $expect_name = shift;
    my $name = shift;

    my $details = grep_app_name($name);

    return grep {$_->{full_path} eq $expect_name} @$details;
}

sub show_status {
    my $separator = "\t  ";

    say "Status${separator}Applictaion";

    for (@$apps) {
        my $dir = dirname $_;
        my $name = basename $_;

        say "@{[active_or_down($_, $name) ? 'Active' : 'Down']} ${separator}$_";
    }
}

sub activate_all {
    say "try to start all apps";

    for (@$apps) {
        my $dir = dirname $_;
        my $name = basename $_;

        unless (active_or_down($_, $name)) {
            my $exec = "";
            $exec = "ruby" if grep {/\.rb/} $name;
            $exec = "python" if grep {/\.py/} $name;

            my $cmd = "cd $dir; nohup $exec ./$name\&";

            say "activate $_";
            system "$cmd>/dev/null 2>&1";
        }
    }

    say "start all apps done";
}

sub stop_all {
    say "not implimented yet";
}

sub show_app_list {
    my $app_list = load_yaml_config();

    for my $idx (0 .. $#{$app_list}) {
        say "$idx: ${$app_list}[$idx]";
    }
}

sub add_app {
    my $name = shift @ARGV;

    if (!defined $name) {
        say "usage:";
        say "$__file__ add foo.bar";
        exit;
    }

    my $app_list = load_yaml_config();
    my $full_path = abs_path $name;
    push @$app_list, $full_path;
    dump_yaml_config($app_list);
    say "add success, current list is:";
    show_app_list();
}

sub del_app {
    my $seq = shift @ARGV;

    if (!defined $seq or $seq =~ /[^\d]+/) {
        say "usage:";
        say "$__file__ del 3";
        exit;
    }

    my $app_list = load_yaml_config();

    if ($seq > $#{$app_list}){
        say "given number out of range";
        say "available: 0 ~ $#{$app_list}";
        show_app_list();
        exit;
    }

    splice @$app_list, $seq, 1;
    dump_yaml_config($app_list);
    say "delete success, current list is:";
    show_app_list();
}

sub main {
    my $command = shift @ARGV;

    if (!defined $command) {
        say "usage:";
        say "$__file__ show/start/stop/list/add/del";
        say "default: show";
        say "";

        show_status();
    }
    elsif ($command eq "show") {
        show_status();
    }
    elsif ($command eq "start") {
        activate_all();
    }
    elsif ($command eq "stop") {
        stop_all();
    }
    elsif ($command eq "list") {
        show_app_list();
    }
    elsif ($command eq "add") {
        add_app();
    }
    elsif ($command eq "del") {
        del_app();
    }
    else {
        say "usage:";
        say "$__file__ show/start/stop/list/add/del";
    }
}

main();


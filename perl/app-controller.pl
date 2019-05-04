#!/usr/bin/env perl

use 5.010;

use YAML;
use Cwd qw/abs_path/;
use File::Basename qw/dirname basename/;
use File::Spec::Functions qw/catfile/;

use Data::Dumper;
# use Data::Dump qw/dump/;

my $__abspath__ = abs_path __FILE__;
my $__dir__     = dirname $__abspath__;
my $__file__    = basename $__abspath__;

my $g_applist_yaml;

sub init {
    my $apm_home = catfile($ENV{"HOME"}, ".apm");

    if (-d $apm_home) {
        $g_applist_yaml = catfile($apm_home, "applist.yml");
    }
    else {
        $g_applist_yaml = catfile($__dir__, "applist.yml");
    }
}

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
        chomp $pid;

        my $cwd = readlink "/proc/$pid/cwd";
        next unless defined $cwd;

        my $exe = readlink "/proc/$pid/exe";
        next unless defined $exe;

        my $cmdline = `cat /proc/$pid/cmdline`;
        my @cmdline_arr = split /\0/, $cmdline;
        my $app_name = $cmdline_arr[1];
        my $full_path = abs_path catfile($cwd, $app_name);

        my $port = `netstat -ntlp 2>/dev/null | grep ${pid} | awk '{print \$4}' | awk -F ':' '{print \$2}'`; chomp $port;
        $port = undef if not $port;

        my $detail = {
            pid => $pid,
            exe => $exe,
            cwd => $cwd,
            app => $app_name,
            port => $port,
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

    say "status:";
    say "-" x 30;
    say "Status${separator}Pid${separator}Port${separator}Applictaion";

    my $app_list = load_yaml_config();

    for (@$app_list) {
        my $dir = dirname $_;
        my $name = basename $_;

        my @items = active_or_down($_, $name);
        my $item = pop @items;

        my $status = $item ? 'Active' : 'Down';
        my $pid = $item->{pid} // "-";
        my $port = $item->{port} // "-";
        my $full_path = $item->{full_path} // $_;

        say "${status}${separator}${pid}${separator}${port}${separator}${full_path}";
    }

    say "-" x 30;
}

sub activate_all {
    say "try to start all apps";

    my $app_list = load_yaml_config();

    for (@$app_list) {
        my $dir = dirname $_;
        my $name = basename $_;

        unless (active_or_down($_, $name)) {
            my $exec = "";
            $exec = "ruby" if grep {/\.rb/} $name;
            $exec = "python" if grep {/\.py/} $name;
            $exec = "perl" if grep {/\.pl/} $name;

            my $cmd = "cd $dir; $exec ./$name>/dev/null 2>&1 \&";

            say " - activate $_";
            system "$cmd";
        }
    }

    say "start all apps done";
    say "";

    show_status();
}

sub stop_all {
    say "try to stop all apps";

    my $app_list = load_yaml_config();
    for (@$app_list) {
        my $expect_name = $_;
        my $dir = dirname $_;
        my $name = basename $_;

        my $details = grep_app_name($name);
        my @matched_items = grep {$_->{full_path} eq $expect_name} @$details;

        for my $item (@matched_items) {
            my $pid = $item->{pid};
            `kill -9 $pid`;
        }
    }

    say "stop all apps done";
    say "";

    show_status();
}

sub show_app_list {
    my $app_list = load_yaml_config();

    say "items:";
    say "-" x 30;

    unless (@$app_list) {
        say "applist is null";
    }

    for my $idx (0 .. $#{$app_list}) {
        say "$idx: ${$app_list}[$idx]";
    }

    say "-" x 30;
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

    if (-d $full_path) {
        say "given path is a directory:";
        say "$full_path";
        exit;
    }

    if (!-f $full_path) {
        say "given path is not an existing file:";
        say "$full_path";
        exit;
    }

    if (grep {/$full_path/} @$app_list)
    {
        say "given path already exist in applist:";
        say "$full_path";
        show_app_list();
        exit;
    }

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

    unless (@$app_list) {
        say "app_list is null";
        say "del cannot be done";
        exit;
    }

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
    init();

    my $command = shift @ARGV;

    if (!defined $command) {
        say "usage:";
        say "$__file__ [command]";
        say "";
        say"[command] can be: show/start/stop/list/add/del";
        say "";
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
    elsif ($command eq "help") {
        say "usage:";
        say "$__file__ [command]";
        say "";
        say "command:";
        say "show:  show app status";
        say "start: start all apps";
        say "stop:  stop all apps";
        say "list:  list all apps with index";
        say "add:   add an app; eg $__file__ add 1";
        say "del:   del an app; eg $__file__ del 1";
        say "help:  show this help";
        say "";
    }
    else {
        say "command cannot be recognized";
        say "";
        say "usage:";
        say "$__file__ show/start/stop/list/add/del";
        say "";
    }
}

main();


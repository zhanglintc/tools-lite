#!/usr/bin/env perl

use 5.010;

use Cwd qw/abs_path/;
use File::Basename qw/dirname basename/;
use File::Spec::Functions qw/catfile/;

my $__file__ = basename __FILE__;

my $apps = [
    "/home/lane/Mmrz-Sync/server/Mmrz-Sync.py",
    "/home/lane/wx-globe/wx-globe.py",
    "/home/lane/navi-site/navi-site.py",
    "/home/lane/lhsjlc4/lhsjlc4.rb",
    "/home/lane/tools-lite/ruby/bingAPI.rb",
    "/home/lane/tools-lite/ruby/returnAddr.rb",
];

sub active_or_down {
    my $expect_name = shift;
    my $name = shift;

    my @pids = `ps -ef | grep -v grep | grep -v vim | grep $name | awk '{print \$2}'`;

    for my $pid (@pids) {
        chomp($pid);

        my $cwd = readlink "/proc/$pid/cwd";
        next unless defined $cwd;

        my $cmdline = `cat /proc/$pid/cmdline`;
        my @cmdline_arr = split /\0/, $cmdline;
        my $app_name = pop @cmdline_arr;

        my $full_path = abs_path catfile($cwd, $app_name);

        return 1 if $full_path eq $expect_name;
    }

    return 0;
}

sub show_status {

    say "Status\t      Applictaion";
    for (@$apps) {
        my $dir = dirname $_;
        my $name = basename $_;

        say "@{[active_or_down($_, $name) ? 'Active' : 'Down']} \t<==>  $_";
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

sub main {
    my $command = shift @ARGV;

    if (!defined $command) {
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
    else {
        say "usage:\n$__file__ show/start/stop";
    }
}

main();


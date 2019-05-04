#!/usr/bin/env perl

use 5.010;

use File::Spec::Functions qw/catfile/;
use Cwd qw/abs_path/;

use Data::Dumper;

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

        my $port = `netstat -ntlp 2>/dev/null | grep ${pid} | awk '{print \$4}' | awk -F ':' '{print \$2}'`;
        chomp $port;

        my $cmdline = `cat /proc/$pid/cmdline`;
        my @cmdline_arr = split /\0/, $cmdline;
        my $app_name = $cmdline_arr[1];
        my $full_path = abs_path catfile($cwd, $app_name);

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

say Dumper grep_app_name("Mmrz-Sync.py")


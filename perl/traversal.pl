#!/usr/bin/perl
use strict;
use warnings;
use Encode qw/from_to/;

my $path = "E:/SVN-Space/leetcode/trunk";
my $filecount = 0;

sub parse_env {
    my $path = $_[0]; #或者使用 my($path) = @_; @_类似javascript中的arguments
    my $subpath;
    my $handle;

    if (-d $path) {#当前路径是否为一个目录
        if (opendir($handle, $path)) {
            while ($subpath = readdir($handle)) {
                if (!($subpath =~ m/^\.$/) and !($subpath =~ m/^(\.\.)$/)) {
                    my $p = $path."/$subpath";

                    if (-d $p) {
                        parse_env($p);
                    }
                    else {
                        ++$filecount;
                        print $p."\n";
                    }
                }
            }
            closedir($handle);
        }
    }

    return $filecount;
}

my $count = parse_env $path;
my $str = "文件总数：".$count;
from_to($str, "utf8", "gbk");

print $str;
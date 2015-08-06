#!/usr/bin/perl
#! -w

use strict;
use warnings;
use 5.012;

$\ = "\n";

my $targetPath = 'E:\Subv_Work\IT5_Color_v3.0\KMSrc_2.06.31\Driver\Model\C658\CUSTOM\SUB\FileNMRast.sub';

open FR, "<", $targetPath or die "Error open file";
while (<FR>) {
    if (/(KOAY..)[^A](.)/) {
        print "$&  =>  $1A$2";
    }
}

open FR, "<", $targetPath or die "Error open file";
my $content;
while (<FR>) {
    $content .= $_;
}
close FR;

$content =~ s/(KOAY..)[^A](.)/$1A$2/g;

open FW, ">", $targetPath or die "Error open file";
print FW $content;
close FW;




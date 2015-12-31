use strict;
use Cwd;
use File::Spec;
use File::Basename;
use utf8;

# Refer to: http://www.chengxuyuans.com/Perl/62287.html
# Refer to: http://www.cnblogs.com/itech/archive/2012/04/28/2468917.html
sub each_file {
    my $givenFolder = shift @_;

    our @pList; # path list to be returned
    &innerEachFile($givenFolder);
    return @pList;

    sub innerEachFile {
        my $path = shift @_;

        if(-d $path) {
            chdir $path or die "can't chdir $path: $!\n";
            foreach (<*>) {
                &innerEachFile(File::Spec->catfile(getcwd, $_));
            }
            chdir (dirname $path) or die "can't chdir ".(dirname $path).": $!\n";
        }
        else {
            push @pList, $path; # push file path into local @pList
        }
    }
}

sub read_all {
    my $target = shift @_;

    open FR, "<", $target or die "Error: $!";

    my $content;
    while (<FR>) {
        $content .= $_;
    }

    return $content;
}

sub write_to {
    my $target = shift @_;
    my $content = shift @_;

    open FW, ">", $target or die "Error: $!";

    print FW $content;
}

sub get_ext {
    my $target = shift @_;

    my $fileName = basename $target;
    my @f = split(/\./, $fileName);

    $f[-1];
}

sub isTarget {
    my $target = shift @_;

    my @ext_list = qw/inf unf ini kmp sub xml/;
    my $ext = lc( &get_ext($target) );
    foreach (@ext_list) {
        if ($ext eq $_) {
            return !undef;
        }
    }

    undef;
}

my $targetFolder = 'E:\Git_Mine\test';
foreach my $target ( &each_file($targetFolder) ) {
    if ( &isTarget($target) ) {
        my $content = &read_all($target);
        $content =~ s/Generic/SINDOH/g;
        $content =~ s|28C-8|D300/D310/CM |g;
        &write_to($target, $content);
        print "replaced: $target\n"
    }
}

<>



use strict;
use Cwd;
use File::Spec;
use File::Basename;

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

    open FR, "<", $_ or die "Error: $!";

    my $content;
    while (<FR>) {
        $content .= $_;
    }

    return $content;
}

my $targetFolder = "/Users/lane/Github/wb";
foreach (&each_file($targetFolder)) {
    my $content = &read_all($_);
    print $content;
}



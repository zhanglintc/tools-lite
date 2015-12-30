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
            my $dir_name = dirname $path;
            chdir $dir_name or die "can't chdir $dir_name: $!\n";
        }
        else {
            push @pList, $path; # push file path into local @pList
        }
    }
}

my $targetFolder = "/Users/lane/Github/leetcode";
foreach (&each_file($targetFolder)) {
    print "$_\n";
}



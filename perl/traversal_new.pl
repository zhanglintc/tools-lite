use strict;
use Cwd;
use File::Spec;
use File::Basename;

# Refer to: http://www.chengxuyuans.com/Perl/62287.html
# Refer to: http://www.cnblogs.com/itech/archive/2012/04/28/2468917.html
sub each_file {
    my $path = shift @_;    

    # 如果是文件夹，进入并遍历
    if(-d $path) {
        chdir $path or die "can't chdir $path:$!";
        foreach (<*>) {
            my $path = File::Spec->catfile( getcwd, $_ );
            &each_file($path);
        }

        # 当前文件夹已经遍历完，回到上一级文件夹
        my $dir_name = dirname $path;
        chdir $dir_name or die "can't chdir $dir_name:$!";
    }
    else {
        print "$path\n";
    }
}

&each_file("E:/Git_Mine");



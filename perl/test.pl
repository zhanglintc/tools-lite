use 5.016;
use YAML qw//;
use Data::Dumper;

my $a = [1,2,3,4];

my $s = YAML::Dump $a;
open my $fw, ">", "config.yml";
print $fw $s;
close $fw;

open my $fr, "<", "config.yml";
my @r = <$fr>;
close $fr;

my $a = YAML::Load "@r";
splice @$a, 1, 1;
say Dumper @$a;


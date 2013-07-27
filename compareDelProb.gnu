set term postscript enhanced eps "Helvetica" 12
set key left bottom spacing 1.3;

set xlabel "Time (in minutes)"
set ylabel "Cumulative Delivery Probability"
set output "Del_prob_1_2.eps";

set xrange[0:86400]
set yrange[0.1:0.7]

plot '1.2_N20F10FM35SM35i2g.txt' using 1:2 title "N20F10FM35SM35" with linespoints lw 3 lt rgb "red",\
'1.2_N20F20FM40SM20i2g.txt' using 1:2 title "N20F20FM40SM20" with linespoints lw 3 lt rgb "blue",\
'1.2_N30F10FM40SM20i2g.txt' using 1:2 title "N30F10FM40SM20" with linespoints lw 3 lt rgb "yellow",\
'1.2_N40F10FM25SM25i2g.txt' using 1:2 title "N40F10FM25SM25" with linespoints lw 3 lt rgb "green",\
'1.2_N50F10FM20SM20i2g.txt' using 1:2 title "N50F10FM20SM20" with linespoints lw 3 lt rgb "black";

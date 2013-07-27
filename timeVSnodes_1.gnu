set term postscript enhanced eps "Helvetica" 12
set key left top spacing 1.3;

set xlabel "Time (in seconds)"
set ylabel "nrOfNodes"
set output "timeVSnodes_1.eps";

set yrange[0:40]
set xrange[0:90000]

plot 'nrOfNodesDetected___s2.1_86400_rwp_1.txt' using 1:2 title "s2.1-24hr_1" with linespoints lw 3 lt rgb "red",\
'nrOfNodesDetected___s2.2_86400_rwp_1.txt' using 1:2 title "s2.2-24hr!1" with linespoints lw 3 lt rgb "blue";

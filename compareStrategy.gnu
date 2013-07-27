set term postscript enhanced eps "Helvetica" 12
#set term png
set nokey

set output "compareStr.eps";

set border 3 front linetype -1 linewidth 1.000
set boxwidth 0.95 absolute
set style fill   solid 1.00 noborder
set grid nopolar
set grid noxtics nomxtics ytics nomytics noztics nomztics \
 nox2tics nomx2tics noy2tics nomy2tics nocbtics nomcbtics
set grid layerdefault   linetype 0 linewidth 1.000,  linetype 0 linewidth 1.000
set key bmargin center horizontal Left reverse noenhanced autotitles columnhead nobox
set style histogram clustered gap 1 title  offset character 2, 0.25, 0
#set style histogram errorbars gap 1 title  offset character 2, 0.25, 0
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by 0  offset character 0, 0, 0
set xtics  norangelimit font ",8"
set xtics   ()
set ytics border in scale 0,0 mirror norotate  offset character 0, 0, 0 
set ztics border in scale 0,0 nomirror norotate  offset character 0, 0, 0 
set cbtics border in scale 0,0 mirror norotate  offset character 0, 0, 0
plot newhistogram "", '1.2delprobReport.txt' using 2:xtic(1) t "1.2" lc rgb "blue",'2.1delprobReport.txt' using 2:xtic(1) t "2.1" lc rgb "red",'2.2delprobReport.txt' using 2:xtic(1) t "2.2" lc rgb "green";

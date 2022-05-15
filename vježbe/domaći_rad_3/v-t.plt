unset multiplot
reset
set encoding utf8

#POSTAVKE GRAFA: DIMENZIJE SLIKE, VELICINA FONTA, IME SLIKE
set term png font "Arial,18pt" size 1000,700 fontscale 1.0 dl 2.0
set output 'v-t.png'

set samples 10000
set bmargin 0.
set lmargin 0.
set rmargin 0.
set tmargin 0.

set style line 1  lt 1 lw 2 lc rgb "#071F61"

set multiplot
  set origin 0.11,0.13 #POMICANJE POCETKA GRAFA KAKO BI STALI OPISI KOORDINATNIH OSI
  set size   0.85,0.85 #VELICINA PODRUCJA U KOJEM ISCRTAVA GRAF (UDIO U 1.0 X 1.0)
    set key top right #POSTAVLJA LEGENDU GORE DESNO
    set grid #KOORDINATNA MREZA
    set xlabel 't[s]'
    set ylabel 'v[m/s]'
    set xrange [0:20]
    set label 1 "k = 1 N/m" at graph 0.05, graph 0.95
    set label 2 "m = 1 kg" at graph 0.05, graph 0.90
    set label 3 "Δt = 0.001 s" at graph 0.05, graph 0.85

    plot 'v-t.dat' w l ls 1

unset multiplot
unset output
set term GNUTERM

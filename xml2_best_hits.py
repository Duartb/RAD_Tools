#!/usr/bin/env python3

# Copyright 2019 Duarte Teomoteo Balata <duarte.balata@gmail.com>
# filter_replicates_vcf.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# filter_replicates_vcf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with keep_central_snps. If not, see <http://www.gnu.org/licenses/>.

import sys

align_file = open(sys.argv[1],"r")
best_hits_file = open(sys.argv[2],"w")
write = False

for line in align_file:

    if line.startswith("#") == True:
        if write == True:
            try:
                best_hits_file.write(best_line[1] + "\n")
                write = False
            except:
                pass
        biggest_percent = 0

    else:
        write = True
        line = line.split("\t")
        if float(line[2]) > biggest_percent:
            biggest_percent = float(line[2])
            best_line = line

best_hits_file.write(best_line[1])
align_file.close()
best_hits_file.close()

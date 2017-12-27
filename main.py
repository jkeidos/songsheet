#! python3
# -*- coding: utf-8 -*-

import glob
import ntpath

# List all song files with extensions relative to chordpro format
exts = ('crd', 'cho', 'pro', 'chordpro', 'chopro')
songfiles = []
for ext in exts:
    aux = glob.glob('.\\sources\\*.' + ext)  # list all song files for the current extension
    songfiles += aux

# Sort file names alphabetically
songfiles.sort

# Generate songbook "CarnetDeChant.sgb" for Songsheet Generator
CARNETfilename = 'CarnetDeChant.sgb'
CARNET = open(CARNETfilename,'w');      # Open the specified file for writing.  Any existing file with this name will be overwritten.
for songfile in songfiles:
    CARNET.write('\"' + ntpath.basename(songfile[1:]) + '\"  Transpose=0 PrintChords=yes\n')
CARNET.close()

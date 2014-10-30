#!/bin/sh
BASEDIR=$(dirname $0)
cd $BASEDIR
# cd ..

# Hide the log.
# mv "dissertation.log" ".logged"

# Remove temporary files.
for TYPE in "*.log" "*.aux" "*.toc" "*.blg" "*.bbl" "*.out" "*.brf" "*.tex-e" "*.lof" "*.lot" "*.loa" ".synctex.gz" ".fdb_latexmk"
do
  rm `find ./ -name $TYPE` -rf
done

cd dissertation/chapters
rm `find ./ -name "*.aux"` -rf
cd ..

cd frontmatter
rm `find ./ -name "*.aux"` -rf
cd ..

cd endmatter
rm `find ./ -name "*.aux"` -rf
cd ..
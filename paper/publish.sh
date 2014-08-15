latexmk main.tex -output-directory=build -pdf
cp build/main.pdf /tmp/
cd ..
git checkout gh-pages
mv /tmp/main.pdf github-process-research.pdf
git commit -am "PDF commit"
git checkout master

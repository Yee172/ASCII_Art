folderpath=$(cd `dirname $0`; pwd)
cd $folderpath
read filename
dot $filename.dot -T png -o $filename.png

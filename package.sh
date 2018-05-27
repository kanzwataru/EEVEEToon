#!/bin/sh

tag=`git describe --tag`
outer_name=eevee-toon_$tag.zip
inner_name=eevee-toon-addon.zip

mkdir -p build/_temp
mkdir -p build/_temp/eevee-toon
cp -R addon/* build/_temp/eevee-toon/
cp -R resources/* build/_temp/eevee-toon/

cd build/_temp/eevee-toon
zip -r ../$inner_name *
cd ../../../

rm -R build/_temp/eevee-toon
cp -R extras/* build/_temp/
cd build/_temp
zip -r ../$outer_name *
cd ../../

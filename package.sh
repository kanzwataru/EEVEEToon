#!/bin/bash
tag=`git describe --tag`
outer_name=eevee-toon_$tag.zip
inner_name=eevee-toon-addon.zip

rm -Rf resources/*.blend1
rm -Rf extras/*.blend1

mkdir -p build/_temp
mkdir -p build/_temp/_inner/eevee-toon
cp -R addon/eevee-toon/* build/_temp/_inner/eevee-toon/
cp -R resources/* build/_temp/_inner/eevee-toon/

pushd build/_temp/_inner
zip -r ../$inner_name *
popd

rm -R build/_temp/_inner
cp -R extras/* build/_temp/
pushd build/_temp
rm -Rf ../$outer_name      # make sure we don't append to existing archive
zip -r ../$outer_name *
popd

rm -R build/_temp

#!/bin/bash
find ./inery.contracts -type f -readable -writable -exec sed -i "s/name1/name2/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/Name1/Name2/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/NAME1/NAME2/g" {} \;
find ./inery.contracts -execdir rename 's/name1/name2/' '{}' \+;
find ./inery.contracts -execdir rename 's/Name1/Name2/' '{}' \+;
find ./inery.contracts -execdir rename 's/NAME1/NAME2/' '{}' \+;

find ./inery.contracts -type f -readable -writable -exec sed -i "s/short_name1/short_name2/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/Short_name1/Short_name2/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/SHORT_NAME1/SHORT_NAME2/g" {} \;
find ./inery.contracts -execdir rename 's/short_name1/short_name2/' '{}' \+;
find ./inery.contracts -execdir rename 's/Short_name1/Short_name2/' '{}' \+;
find ./inery.contracts -execdir rename 's/SHORT_NAME1/SHORT_NAME2/' '{}' \+;

#!/bin/bash
find ./<dir> -type f -readable -writable -exec sed -i "s/name1/name2/g" {} \;
find ./<dir> -type f -readable -writable -exec sed -i "s/Name1/Name2/g" {} \;
find ./<dir> -type f -readable -writable -exec sed -i "s/NAME1/NAME2/g" {} \;
find ./<dir> -execdir rename 's/name1/name2/' '{}' \+;
find ./<dir> -execdir rename 's/Name1/Name2/' '{}' \+;
find ./<dir> -execdir rename 's/NAME1/NAME2/' '{}' \+;

find ./<dir> -type f -readable -writable -exec sed -i "s/short_name1/short_name2/g" {} \;
find ./<dir> -type f -readable -writable -exec sed -i "s/Short_name1/Short_name2/g" {} \;
find ./<dir> -type f -readable -writable -exec sed -i "s/SHORT_NAME1/SHORT_NAME2/g" {} \;
find ./<dir> -execdir rename 's/short_name1/short_name2/' '{}' \+;
find ./<dir> -execdir rename 's/Short_name1/Short_name2/' '{}' \+;
find ./<dir> -execdir rename 's/SHORT_NAME1/SHORT_NAME2/' '{}' \+;

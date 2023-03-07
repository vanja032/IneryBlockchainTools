#!/bin/bash
find ./inery.contracts -type f -readable -writable -exec sed -i "s/eosio/inery/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/Eosio/Inery/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/EOSIO/INERY/g" {} \;
find ./inery.contracts -execdir rename 's/eosio/inery/' '{}' \+;
find ./inery.contracts -execdir rename 's/Eosio/Inery/' '{}' \+;
find ./inery.contracts -execdir rename 's/EOSIO/INERY/' '{}' \+;

find ./inery.contracts -type f -readable -writable -exec sed -i "s/eos/ine/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/Eos/Ine/g" {} \;
find ./inery.contracts -type f -readable -writable -exec sed -i "s/EOS/INE/g" {} \;
find ./inery.contracts -execdir rename 's/eos/ine/' '{}' \+;
find ./inery.contracts -execdir rename 's/Eos/Ine/' '{}' \+;
find ./inery.contracts -execdir rename 's/EOS/INE/' '{}' \+;
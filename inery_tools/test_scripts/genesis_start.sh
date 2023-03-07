#!/bin/bash
DATADIR="./blockchain"

if [ ! -d $DATADIR ]; then
  mkdir -p $DATADIR;
fi

nodine \
--genesis-json $DATADIR"genesis.json" \
--plugin inery::producer_plugin \
--plugin inery::producer_api_plugin \
--plugin inery::chain_plugin \
--plugin inery::chain_api_plugin \
--plugin inery::http_plugin \
--plugin inery::history_api_plugin \
--plugin inery::history_plugin \
--plugin inery::net_plugin \
--plugin inery::net_api_plugin \
--filter-on=* \
--data-dir $DATADIR"/data" \
--blocks-dir $DATADIR"/blocks" \
--config-dir $DATADIR"/config" \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
--p2p-max-nodes-per-host 100 \
--connection-cleanup-period 10 \
--producer-name inery \
--http-server-address 0.0.0.0:8888 \
--p2p-listen-endpoint bis.blockchain-servers.world:9010 \
--signature-provider INE6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV=KEY:5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3 \
>> $DATADIR"/nodine.log" 2>&1 & \
echo $! > $DATADIR"/ined.pid"
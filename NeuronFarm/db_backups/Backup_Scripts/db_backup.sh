#!/bin/bash
PGPASSWORD='zelda' pg_dump -U grey -h localhost neuronfarm > //home/ncacord/Desktop/Raphael/NeuronFarm/db_backups/neuronfarm_backup_$(date +"%Y%m%d").sql




     alarm: bind_rndc_named_name_server_statistics
        on: bind_rndc_named.name_server_statistics
     units: stats
     every: 60
    lookup: sum -5s unaligned absolute of nms_requests
      calc: $nms_requests
      warn: $this < 50
      crit: $this < 0
      info: Query request is to low! Consider to create logrotate conf file for it!
        to: sysadmin

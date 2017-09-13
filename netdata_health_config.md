# health configuration reference

alarm or template
This line has to be first on each alarm or template

1.**alarms**, which are attached to specific charts

2.**templates**, which define rules that should be applied to all charts having a specific `context`.

--------------------------------------------------------------------------------
on :
defines the data the alarm should be attached to.

on: CHART  (alarm)
For CHART you can use a chart id or name of the chart, as shown on the dashboard

on:CONTEXT (template)
CONTEXT is the template of a chart. find the `CONTEXT` of a chart download the latest `netdata.conf`, find the chart you are interested and you will see its context in its configuration section. You can also find it if you fetch `http://your.netdata:19999/api/v1/charts`



--------------------------------------------------------------------------------

families

This line is only used in alarm templates.

--------------------------------------------------------------------------------

lookup

lookup: METHOD           AFTER            [at BEFORE]     \[every DURATION]      \[OPTIONS]            \[ of DIMENSIONS]
        average          -1s     default 0    updated frequencyy   percentage     optional   have to be ,or |                        
        mix              -1m                                       absoleteon
        max              -1h                                       min2max                  
        sum              -1d                                       unaligned
        incremental-sum                                                 

--------------------------------------------------------------------------------

calc

call EXPRESSION

The result of the calculation will be available as `$this` in warning and critical expressions 



***



#### `green`  and  `red`

```
green: NUMBER
red: NUMBER
```

Set the green and red thresholds of a chart. Both are available as `$green` and `$red` in expressions. 



--------------------------------------------------------------------------------

every

Sets the update frequency of this alarm

--------------------------------------------------------------------------------

warn and crit

They trigger the alarm. Both are optional

--------------------------------------------------------------------------------

to

to: ROLE1 ROLE2 ROLE3 ...

This will be the first parameter of the script to be executed when the alarm switches status

--------------------------------------------------------------------------------

exec 

exec: SCRIPT

--------------------------------------------------------------------------------

delay

delay: [[\[up U][down D] multiplier M] max X]



http://your.netdata.ip:19999/api/v1/alarm_variables?chart=NAME
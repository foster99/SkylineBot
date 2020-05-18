grammar Skyline; //

root : (asigancion | skyline) EOF;

asigancion :
      WORD ':=' skyline
    | WORD ':=' '[' skyline_list ']'
    | WORD ':=' '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}'
    ;

skyline :
      '(' skyline ')'
    | '-' skyline
    | skyline ('+'|'-'|'*') NUM
    | skyline ('+'|'*') skyline
    | '[' skyline_list ']'
    | skyline_root
    ;

skyline_root : ('(' NUM ',' NUM ',' NUM ')') | WORD;

skyline_list : skyline (',' skyline)* ;

NUM : [0-9]+;
WS  : [ \n]+ -> skip;
WORD : [a-zA-Z][0-9a-zA-Z]*;
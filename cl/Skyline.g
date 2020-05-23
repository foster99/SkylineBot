grammar Skyline; //

root : (assignment | temp_skyline) EOF;

assignment : WORD ':=' skyline;
temp_skyline : skyline;

skyline :
      '(' skyline ')'
    | mirror skyline
    | skyline (translate_r|translate_l|replicate) NUM
    | skyline (union|intersection) skyline
    | existing_skyline
    | '{' random_skyline '}'
    | '[' building_list ']'
    | '(' building ')'
    ;

mirror : '-';
intersection: '*';
union : '+';
translate_r : '+';
translate_l : '-';
replicate : '*';

existing_skyline : WORD;
random_skyline : NUM ',' NUM ',' NUM ',' NUM ',' NUM ;
building : NUM ',' NUM ',' NUM;

building_list : '(' building ')' (',' '(' building ')')* ;

NUM : [0-9]+;
WS  : [ \n]+ -> skip;
WORD : [a-zA-Z][0-9a-zA-Z]*;
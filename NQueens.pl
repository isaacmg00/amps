% Isaac Garcia NQueens Prolog solution

nc([H|T]) :-
    nc(H,T,1).

nc(_,[],_).
nc(P,[H|T],D):-
    P \= H,
    RDIFF is abs(P-H),
    RDIFF \= D,
    DP1 is D+1,
    nc(P,T,DP1).

solve(N,X):-
    solve(N,[],X).
solve(N,X,X):-
    length(X,N).
solve(N,T,X):-
    NM1 is N-1,
    between(0,NM1,P),
    append([P],T,T2),
    nc(T2),
    solve(N,T2,X).
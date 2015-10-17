dom = ["1","2","3","4"]

fails = 0
    
for A in dom:
    for B in dom:
        for C in dom:
            for D in dom:
                for E in dom:
                    if E!=C:
                        if int(E) < (int(D)-1):
                            for F in dom:
                                if abs(int(F)-int(B)) == 1:
                                    if C!=F:
                                        if D!=F:
                                            if abs(int(E)-int(F))%2 !=0:
                                                for G in dom:
                                                    if A > G:
                                                        if G!=F:
                                                            if D!=C:
                                                                if abs(int(G)-int(C))==1:
                                                                    for H in dom:
                                                                        if A <= H:
                                                                            if G < H:
                                                                                if (int(H)-int(C)) % 2==0:
                                                                                    if H!=D:
                                                                                        if E!=(int(H)-2):
                                                                                            if F!=H:
                                                                                                print(A, B, C, D, E, F, G, H, "solution")
                                                                                            else:
                                                                                                fails +=1
                                                                                        else:
                                                                                            fails +=1
                                                                                    else:
                                                                                        fails +=1
                                                                                else:
                                                                                    fails +=1
                                                                            else:
                                                                                fails +=1
                                                                        else:
                                                                            fails +=1
                                                                else:
                                                                    fails +=1
                                                            else:
                                                                fails +=1
                                                        else:
                                                            fails +=1
                                                    else:
                                                        fails +=1
                                            else:
                                                fails +=1
                                        else:
                                            fails +=1
                                    else:
                                        fails +=1
                                else:
                                    fails +=1
                        else:
                            fails +=1
                    else:
                        fails +=1
                
print("number of failures:",fails)
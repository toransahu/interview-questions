
    /*
     * Complete the function below.
     */
    static int getCountOfPossibleTeams(int[] coders) {
        int fist = 0;
        int sec = 0;
        int third = 0;
        int res = 0;
        for(int i=0; i<coders.length;i++){
            for(int j=i+1; j<coders.length;j++){
                for(int k=j+1; k<coders.length;k++){
                    if(coders[i]>coders[j] && coders[j]>coders[k])
                        res = res + 1;
                }
            }
        }

        int[] rev = new int[coders.length];
        for(int i=coders.length-1; i>=0;i--){
            rev[i]=coders[i];
        }

        for(int i=0; i<rev.length;i++){
            for(int j=i+1; j<rev.length;j++){
                for(int k=j+1; k<rev.length;k++){
                    if(rev[i]<rev[j] && rev[j]<rev[k])
                        res = res + 1;
                }
            }
        }
        return res;
    }

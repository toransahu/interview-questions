
    /*
     * Complete the function below.
     */
    static String[] getShrunkArray(String[] inputArray, int burstLength) {
        int count = 0;
        //int MAX_INTEGER = 200;
        ArrayList<String> repeatedArray = new ArrayList<String>();




        for( int i=0; i< inputArray.length; i++){
            repeatedArray.add(inputArray[i]);
        }


        for( int i=0; i< inputArray.length; i++){
            for( int j=i+1; j< inputArray.length; j++){
                if (inputArray[i].equals(inputArray[j])){
                    count++;

                }}
            if (count>=3){
                repeatedArray.remove(inputArray[i]);
            }
        }

        Integer res_size = repeatedArray.size();
        String[] res = new String[res_size];
        Integer idx=0;
        for (String e:repeatedArray){
                //System.out.println(e);
                res[idx]=e;
                idx++;

            }
        //System.out.println(repeatedArray);
    return res;
    }

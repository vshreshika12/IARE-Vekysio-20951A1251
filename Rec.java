import java.util.*;
public class Rec_word{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String sent = sc.nextLine();
        System.out.println(Each_word(sent));
    }
    public static String Each_word(String sent)
    {
        if(sent.isEmpty())
        {
            return sent;
        }
        
        int index = sent.indexOf(" ");
        if(index==-1)
        {
            return str1_rev(sent)+" ";
            
        }
        String word = sent.substring(0,index);
        String left_sent=sent.substring(index+1);
        return str1_rev(word)+" "+Each_word(left_sent);
    }
    public static String str1_rev(String word)
    {
        if(word.isEmpty())
        {
            return word;
        }
        return str1_rev(word.substring(1))+word.charAt(0);
    }
        
    }

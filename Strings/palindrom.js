// 1.Plaindrome Check

// Q.Write a function that takes in a non-empty string and that returns a boolean
// representing whether the string is a palindrome.
// A palindrome is defined as a string that's written the same forward and
// backward. Note that single-character strings are palindromes.

//   sample input

//    = "abcdcba"

//    o/p : true


//solution 1

const isPlaindrome=(string)=>{



    let reversedString='';

    for(let i=string.length-1;i>=0;i--){
        reversedString+=string[i]
    }

    return string === reversedString



}







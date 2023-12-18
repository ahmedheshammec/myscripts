
#!/bin/bash

# Set the length of the password
length=8

# Set the list of words to use
words=("Troy" "Hunt" "Alpha" "Charley" "Beta" "Cyber" "Eagle" "Black" "Cyberstorm" 
       "Byte" "Hero" "Serpent" "Ghost" "Digital" "Code" "Code" "Binary" "Binary" 
       "Ninja" "Viper" "Phoenix")

# Set the list of numbers to use
numbers=("0" "1" "2" "3" "4" "5" "6" "7" "8" "9")

# Set the list of special characters to use
characters=("@" "#" "$" "%" "&")

# Calculate the number of words in the list
num_words=${#words[@]}

# Calculate the number of numbers in the list
num_numbers=${#numbers[@]}

# Calculate the number of special characters in the list
num_characters=${#characters[@]}

# Initialize the password
password=""

# Pick a random word with a capital letter
word=""
while [[ ! "$word" =~ ^[A-Z] ]]; do
  word=$(echo ${words[$(($RANDOM % ${#words[@]}))]})
done
word=$(echo $word | tr '[:lower:]' '[:upper:]')

# Append the word to the password
password=$word

# Add one number and one special character to the password
password="$password${numbers[$(($RANDOM % $num_numbers))]}${characters[$(($RANDOM % $num_characters))]}"

# Create the rest of the password by selecting random words and numbers from the lists
for i in $(seq 1 $(($length - 3)))
do
  # Generate a random number to decide whether to use a word, a number or a special character
  use_type=$((RANDOM % 3))

  if [ $use_type -eq 0 ]
  then
    # Generate a random index between 0 and the number of words
    index=$(($RANDOM % $num_words))

    # Append the lowercase version of the word at the chosen index to the password
    password="$password${words[$index]}"
  elif [ $use_type -eq 1 ]
  then
    # Generate a random index between 0 and the number of numbers
    index=$(($RANDOM % $num_numbers))

    # Append the number at the chosen index to the password
    password="$password${numbers[$index]}"
  else
    # Generate a random index between 0 and the number of special characters
    index=$(($RANDOM % $num_characters))

    # Append the special character at the chosen index to the password
    password="$password${characters[$index]}"
  fi
done

# Print the password
echo "| Password: $password |"

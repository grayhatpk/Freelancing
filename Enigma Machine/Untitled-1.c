#include <stdio.h>
#include <stdlib.h>
#include<ctype.h>
#include<string.h>
#include<unistd.h>

void plugboard(char *plain_text,char plugchar[],char plug_subs[]){ // implementing the plugboard susbstitution
	
	char * temp=plain_text; // temporarely storing the starting address of text given to the plugboard
	
	int len=strlen(plain_text);
	
	while(*plain_text!='\0'){ 					// this loop is converting the text to upper case letters. All the substitution in the 
												// machine is carried out in the capital lettes. 
		*plain_text = toupper(*plain_text);
		plain_text++;
    }
		plain_text=temp; 			//setting back the address of the first element to the variable
	
	for(int i=0;i!=len;i++){		// This is the main loop which is implementing the plugboard subst
	 		
		if(plain_text[i]==' '){		// if there is space in the text then repalce it with the . 	
			plug_subs[i]='.';  
		}
		else if(plain_text[i]=='.'){ //at the decryption if the character is . then convert it back to the ' ' space 
			plug_subs[i]=' ';    
		}
		else
			plug_subs[i]= plugchar[(int)plain_text[i] - 65];	// plug the substitution of the plugboard at the value
																// calculated according to the letter asscii character	  
   }
   //char plugchar[27]={'Z','P','H','N','M','S','W','C','I','Y','T','Q','E','D','O','B','L','R','F','K','U','V','G','X','J','A'};
   	// to check what is the plugboard subsitution this is for testing purpose no need in the program actual implemtation  
	/*printf("\n\n-------------------------------------------------------------------------");
	printf("\n\t\t\tplugboard substutution --> %s",plug_subs); //plugboard substutution till that point 
	printf("\n---------------------------------------------------------------------------\n ");*/
}

char validation(char value){ // this function is checking for the validation. If there is other charachter given at any point in the input 
	while(!(isalpha(value))){	// other than the character. Then this function will tell the user to input that character again. 	
		printf("\n\t\t\t---------Only Character is allowed---------------");
		getchar();	
		value=getchar();
	}
	return value;
}

void change_rotor_subs(char rotor_subs[],char rotor_pos){  // This function is setting the position of the rotors according to the user given
															// rotors substitution in the machine 
	rotor_pos = toupper(rotor_pos);
	int i,temp=0;
	int pos = (int)rotor_pos-65;
	
	char rotor_change_subs[26];

	for (i=pos;i<26;i++){ // loop for changing the position of the right rotor substitioun to new one  	
		rotor_change_subs[i]=rotor_subs[temp];
		temp++;
	}
	
	// if the user has given the initial rotor position  to D then the subsitution K will be the respective substutiution for the D
	//now for fixing the substution of the remianng characters in the array
	
	for(int j=0;j<pos;j++){
		rotor_change_subs[j]=rotor_subs[temp];
		temp++;
	}
	strcpy(rotor_subs,rotor_change_subs);	 // copied the changed substitution back to the orignal . now the original substitution has changed 
}

int find_char_pos(char rotor[],char ch){
	int pos=0;
	for (int i=0;i<26;i++){
		if(rotor[i]==ch){
			pos=i;
			break;
		}
	}
	return pos;
}

char reflection(char text){  // this function will return back the appropiate substitution for the text on the reflector of machine 
	
	char reflection_subs[26]={'Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E' ,'B', 'F', 'Z', 'C','W','V','J','A','T'};
    
	char encrypt = reflection_subs[((int)text) -65];
    
    return encrypt;    
}

char left_rotor(char encrypt,char lrotor_subs[]){ // this function is performing subsitution through the rotors left wheel. Each character is substituted from it's position from the array of left rotor substitution 
int pos=0;
char encrypt_text=lrotor_subs[((int)encrypt)-65];
	
	encrypt_text=reflection(encrypt_text);
	
	pos=find_char_pos(lrotor_subs,encrypt_text);
	
	return ((char) 65+pos);
}

char middle_rotor(char plug_subs,char mrotor_subs[],char lrotor_subs[]){ // This function is substituting the middle rotor characters against the right rotor given output
	int pos=0;
	char encrypt_text = mrotor_subs[((int) plug_subs)-65] ;
		
	encrypt_text = left_rotor(encrypt_text,lrotor_subs);
	
	pos=find_char_pos(mrotor_subs,encrypt_text);
	
	return ((char) (65+pos));
}

char plugboard_subs(char ch,char plug_subs[]){ 

	int pos=0;
	pos=find_char_pos(plug_subs,ch);
	ch = (char)(pos+65);	
	return ch;
}

char right_rotor(char plug_subs,char rrotor_subs[],char mrotor_subs[],char lrotor_subs[],char plug_char[]){ // This function is substituting the appropriate characters agianst the plugboard given output
	
	int length = (int)plug_subs-65,pos=0;
	char ch,encrypt_text;
	
	encrypt_text = rrotor_subs[length];
	
	encrypt_text = middle_rotor(encrypt_text,mrotor_subs,lrotor_subs);
	pos=find_char_pos(rrotor_subs,encrypt_text);
	encrypt_text=(char) pos+65;
	
	encrypt_text=plugboard_subs(encrypt_text,plug_char);
	
	return encrypt_text;
}


int main() {

	char *plain_text, lrotor_pos, mrotor_pos, rrotor_pos,ex;    // declare a pointer to a character
    
	char rrotor_subs[26]={'K', 'M','T','F', 'O', 'I', 'X', 'W', 'V', 'U', 'B','A','Q','P','N','Y','E','C','R','J','S','L','Z','H','G','D'};
    //These are the characters for substitution in the rotor III
    char mrotor_subs[26]={'V', 'Z', 'Y', 'X', 'W', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'};
    
	char lrotor_subs[26]={'A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'};

	int length = 1, i = 0, text_length,choice;   // initialize the size to 1
    char plugchar[27]={'Z','P','H','N','M','S','W','C','I','Y','T','Q','E','D','O','B','L','R','F','K','U','V','G','X','J','A'};
    plain_text = (char*) malloc(length);   // allocate 1 byte of memory for tex 	

	printf("\n------------------------------------------------------------------------------ ");   
    printf("\n\t\t Give Input to the Machine -->  : \n ");
	while (1) {
        char c = getchar();   // read one character at a time
        	
        if (c == '\n') {   // check if the user has pressed enter
            plain_text[i] = '\0';   // replace the newline character with the null character
            break;   // exit the loop
        }
        plain_text[i] = c;   // store the character in the text array
        	i++;   // increase the index of text by 1
        if (i == length) {   // check if the text array is full
            length += 1;   // increase the size of text by 1
            plain_text = (char*) realloc(plain_text, length);   // reallocate memory for text
            
			if (plain_text == NULL) {   // check if reallocation failed
                printf("Error: Memory allocation failed!\n");
                return 1;
            }
        }
    }
    
   	printf("\n------------------------------------------------------------------------------ \n\n");
    
	printf("\n\t Give the Right Rotor Starting Point -------> ");
    rrotor_pos=getchar();
	if(!(isalpha(rrotor_pos)))
    	rrotor_pos=validation(rrotor_pos);
    
		
    printf("\n\n\t Give the Middle Rotor Starting Point -------> ");
    getchar();
	mrotor_pos=getchar();
	
	if(!(isalpha(mrotor_pos)))
    	rrotor_pos=validation(mrotor_pos);
    
    
	printf("\n\t Give the left Rotor Starting Point -------> ");
    getchar();
	lrotor_pos=getchar();
	lrotor_pos=validation(lrotor_pos);
	
	printf("\n--------------------------------------------------------------------------------\n");
    
    if(toupper(rrotor_pos)!='A'){ // if the given rotor position is not A then change the left rotor substitution
	 	change_rotor_subs(rrotor_subs,rrotor_pos);
	}

    if(toupper(mrotor_pos)!='A'){
    	change_rotor_subs(mrotor_subs,mrotor_pos);	
	}

	if(toupper(lrotor_pos)!='A'){
		change_rotor_subs(lrotor_subs,lrotor_pos);
	}
	
	char plug_subs[strlen(plain_text)]; // this will store the plugboard substitution of the plain_text 
	
	char encrypt_text[strlen(plain_text)]; // this will store the encrypted text by the rotors
		
	plugboard(plain_text,plugchar,plug_subs); // calling the plugboard function    	
	// starting loop for the rotors
	getchar();
	for(int i=0; i<strlen(plug_subs);i++){
		
		if(plug_subs[i]=='.')
			encrypt_text[i] = plug_subs[i];
		else if(plug_subs[i]==' ')
			encrypt_text[i]=' ';	
		else 
			encrypt_text[i]=right_rotor(plug_subs[i],rrotor_subs,mrotor_subs,lrotor_subs,plugchar);
		}
		
	printf("\t The Output of the Enigma Machine -> ");
	
	for(int i=0;i<strlen(plug_subs);i++)	
   	  printf("%c",encrypt_text[i]);
		 
	printf("\n--------------------------------------------------------------------------------\n");     	
    
    printf("\n ----------------------------  ");
    printf("\n Press \n g. GO BACK \n e. EXIT \n  -------> ");

	ex=getchar();
    ex=validation(ex);
    
	if(ex=='g'){
		system("CLS");
		getchar();
		free(plain_text);      	
		main();
	}
	else{
		printf("\n\t\t Exiting ............");
    	exit(0); 
    }
    
	free(plain_text);   
    return 0;
}

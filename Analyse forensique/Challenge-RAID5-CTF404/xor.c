#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>


struct global_v {
	int tamano;
	int * arreglo2;
} global_v;


static struct option long_options[] = {
 	{"result", required_argument, 0, 'r'},
    {"help", no_argument, 0, 'h'},
    {"version", no_argument, 0, 'v'},	
    {0, 0}
};


static void uso() {
    fprintf(stderr, 
		"XOR for files\n"
		"Usage: \n"
		"xor [-r \"path\"] path_1 path_2 (...) path_n \n"
		"Where:\n"
		"    -h, --help             Usage\n"
		"    -r, --result           Resultant file path\n"
		"    -v, --version          Show version of the program\n"
	);
}


int xor_op(FILE * archivo2, int *arreglo) {
	int d, i;
	i = 0;
	d = fgetc(archivo2);
    while(i != global_v.tamano) {
		global_v.arreglo2[i] = arreglo[i]^d;
        i++;
       	if(d == EOF) {
       		rewind(archivo2);
       	}	
        d = fgetc(archivo2);
    }
	fclose(archivo2);	
}


int main(int argc, char *argv[]) {	
	int args, i;
	char *ruta = NULL;
	global_v.tamano = 0;
	args = 0; 
	int index;
	int ruta_ind = 0;
	int option_index = 0;
	FILE *archivo;
	FILE *archivo2;
	
	
	while (1) {
		args = getopt_long(argc, argv, "r:h?v", long_options, &option_index);
		
	    if (args == -1) {
        	break;
        }
        
        switch (args) {
        	case 'r':
        		ruta = (char*)optarg;
        		ruta_ind = 1;
        		break;
        	case 'v':
        		fprintf(stdout, "XOR V1.0	Endrey Diaz		01-21-2014\n");
        		break;
        	case 'h':
        	case '?':
            	uso();
            	return 0;       		
        	default:
        		fprintf(stderr, "ERROR: Invalid argument\n");
        		uso();
        		return 1;
        }
    }
    
	if (argc == 1) {
		uso();
		return 1;
	}
	
	if ((ruta == NULL) && (ruta_ind == 1 )) {
		fprintf(stderr, "ERROR: Invalid path. Please specify\n");
		uso();
		return 1; 
	}
	
	if (ruta != NULL) { 
		if (strcmp(ruta, "-h") == 0) {
			fprintf(stderr, "ERROR: Invalid path. Please specify\n");
			uso();
			return 1; 
		}
	}

	index = 3;   
	if (ruta_ind == 0) {
		index = 3;
	}    	    
        
	for (optind; optind < argc; optind++) {
		if ((argv[optind] != NULL) && (index == 3)) {
			archivo = fopen(argv[optind], "r");
			if (archivo == NULL) {
				fprintf(stderr, "ERROR: Invalid path for first file\n");
				uso();
				return 1;
			}
			fseek(archivo, 0, SEEK_END);
			global_v.tamano = ftell(archivo);
			rewind(archivo);
			i = 0;
			global_v.arreglo2 = (int *)malloc (global_v.tamano*sizeof(int));
			while (i != global_v.tamano) {
		   		global_v.arreglo2[i] = fgetc(archivo);
				i++;
			}
			fclose(archivo);
			optind++;
			index++;
		}

		if ((argv[optind] == NULL) && ((index == 4)||(index == 3))) {
		 	fprintf(stderr, "ERROR: Two files at least required\n");
			return 1;
		}

		if ((argv[optind] != NULL) && (index > 3)) {
			archivo2 = fopen(argv[optind], "r");
	   		if (archivo2 == NULL) {
	   		    fprintf(stderr, "ERROR: Invalid path for file %i \n", optind-2);
				uso();
				return 1;
			}
		}
		index++;
	   	xor_op(archivo2, global_v.arreglo2);	  
	}

	i = 0;
	if (ruta_ind == 1) {
		archivo = fopen(ruta, "w+");
		while (i < global_v.tamano) {
			fputc(global_v.arreglo2[i], archivo);
			i++;
		}
		fclose(archivo);
	}
	else {
		while (i < global_v.tamano) {
			fprintf(stdout, "%c", (char)global_v.arreglo2[i]);
			i++;
		}
	}
	 	
	free(global_v.arreglo2);
      	
}

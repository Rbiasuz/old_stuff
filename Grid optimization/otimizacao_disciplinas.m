% clear all
clear nx_dados
clear tx_dados
nome_arquivo = 'ementas.xlsx';
aba = 'Planilha1';
 
% Leitura dos dados
[nx_dados,tx_dados] = xlsread(nome_arquivo,aba);
 
% Criação da matriz de palavras.
col_titulos = 1;
matriz_palavras_binaria = [];
for i = 1:size(tx_dados,1)
    texto_temp = tx_dados{i,col_titulos};
    cont_letras = 0;
    cont_palavras = 1;
    palavra_temporaria = '';
    for j = 1:size(texto_temp,2)
        if strcmp(texto_temp(j),' ') == 1
            matriz_palavras{i,cont_palavras} = palavra_temporaria;
            matriz_palavras_binaria(i,cont_palavras) = 1;
            cont_palavras = cont_palavras + 1;
        else
            palavra_temporaria = strcat(palavra_temporaria,texto_temp(j));
        end
        if strcmp(texto_temp(j),' ') == 1
            palavra_temporaria = '';
        end
        if size(texto_temp,2) == j
            matriz_palavras{i,cont_palavras} = palavra_temporaria;
            matriz_palavras_binaria(i,cont_palavras) = 1;
        end
    end
end

%Vetor unico 
clear matriz_string
cont = 0;
clear vetor_string
for i =1:size(matriz_palavras,1)
    for j =1:size(matriz_palavras,2)
        if matriz_palavras_binaria(i,j) == 1
            cont = cont + 1;
            vetor_string(cont) = matriz_palavras(i,j);
        end
    end
end
vetor_unico_texto = unique(vetor_string);
 
%Contador de repetições do vetor unico 
for k=1:length(vetor_unico_texto)
    aux=0;
    for i = 1:size(matriz_palavras,1)
        for j = 1:size(matriz_palavras,2)
            if strcmpi(matriz_palavras(i,j),vetor_unico_texto(k)) == 1
                aux=aux+1;
            end
        end
    end
    vet_unico_cont(k)=aux;
end
 
% retirar palavras
vetor_retirar = {'-','a','à','e','é','o','I:','I','II','II:','III','III:','IV','IV:','V','VI','por','em','na','para','da','das','de','do','dos','curso','conclusão','estágio','para','um','uma','na','no', 'ainda', 'além', 'ambas', 'ambos', 'antes', 'ao', 'aonde', 'aos', 'após','aquele', 'aqueles', 'as', 'assim', 'com', 'como', 'contra', 'contudo', 'cuja', 'cujas', 'cujo', 'cujos', 'da', 'das', 'de', 'dela', 'dele', 'deles', 'demais', 'depois', 'desde', 'desta', 'deste', 'dispõe', 'dispoem', 'diversa','diversas', 'diversos', 'do', 'dos', 'durante', 'e', 'ela', 'elas', 'ele', 'eles', 'em', 'entao', 'entre', 'essa', 'essas','esse', 'esses', 'esta', 'estas', 'este', 'estes', 'ha', 'isso', 'isto', 'logo', 'mais', 'mas', 'mediante', 'menos','mesma', 'mesmas', 'mesmo', 'mesmos', 'na', 'nas', 'não', 'nas', 'nem', 'nesse', 'neste', 'nos', 'o', 'os', 'ou','outra', 'outras', 'outro', 'outros', 'pelas', 'pelas', 'pelo', 'pelos', 'perante', 'pois', 'por', 'porque','portanto', 'proprio', 'propios', 'quais', 'qual', 'qualquer', 'quando', 'quanto', 'que', 'quem', 'quer', 'se','seja', 'sem', 'sendo', 'seu', 'seus', 'sob', 'sobre', 'sua', 'suas', 'tal', 'tambem', 'teu', 'teus', 'toda', 'todas','todo', 'todos', 'tua', 'tuas', 'tudo'};
for i = 1:size(matriz_palavras,1)
    for j = 1:size(matriz_palavras,2)
        for k = 1:size(vetor_retirar,2)
            if strcmpi(matriz_palavras(i,j),vetor_retirar(k))==1
                matriz_palavras(i,j)={''};
            end
        end
    end
end
 
%retirar espaços1
matriz_aux={0};
for i=1:size(matriz_palavras,1)
    aux=0;
    for j=1:size(matriz_palavras,2)
        if strcmp(matriz_palavras(i,j),'') == 0
            aux=aux+1;
            matriz_aux(i,aux)=matriz_palavras(i,j);
         end
    end
end
matriz_palavras=matriz_aux;

%Removendo palavras repetidas por linha
matriz_aux=(matriz_palavras);
for i =1:size(matriz_palavras,1)
    vetor_string=matriz_palavras(i,:);
    for j = 1:size(vetor_string,2)
        palavra1=vetor_string(j);
        cont=0;
        for k = j:-1:1
            palavra2=vetor_string(k);
            if strcmpi(palavra1,palavra2) == 1 && strcmp(palavra1,'') == 0
                cont=cont+1;
            end
            if cont >= 2
                vetor_string{j}=''
            end
        end
    end    
    matriz_aux(i,:)=vetor_string;
end

%retirar espaços2
matriz_palavras={0};
aux=max(vetor_quanti_palavras);
for i = 1:size(matriz_aux,1)
    for j = 1:aux
        matriz_palavras(i,j)=matriz_aux(i,j);
    end
end
 
%Matriz de comparações1
matriz_numeros = zeros(size(matriz_palavras,1),size(matriz_palavras,2));
matriz_numeros_binaria = zeros(size(matriz_palavras,1),size(matriz_palavras,2));
vetor_quanti_palavras = zeros(size(matriz_palavras,1),1);
for i = 1:size(matriz_palavras,1)
    for j = 1:size(matriz_palavras,2)
        for k = 1:length(vetor_unico_texto)
            if strcmpi(matriz_palavras(i,j),vetor_unico_texto(k)) == 1
                matriz_numeros(i,j) = vet_unico_cont(k);
                matriz_numeros_binaria(i,j) = 1;
            end
        end
    end
    vetor_quanti_palavras(i) = sum(matriz_numeros_binaria(i,:));
end
 
%Matriz de comparações2
clear matriz_contador
for i = 1:size(matriz_palavras,1)
    for k = 1:size(matriz_palavras,1)
        cont = 0;
        for j =1:size(matriz_palavras,2)
            palavra1 = matriz_palavras(i,j);
            for l = 1:size(matriz_palavras,2)
                palavra2 = matriz_palavras(k,l);
                if  strcmpi(palavra1,palavra2) == 1 && strcmp(palavra1,'') == 0
                    cont = cont +1;
                end
            end
        end
            matriz_contador(i,k) = cont/vetor_quanti_palavras(i);
    end
    
end

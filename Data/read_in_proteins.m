function [proteinName,affinity,ligandName]=read_in_proteins()
%load_path should be the full path [pwd '\' exper{j}]
load_path='/Users/wenyun/Downloads/plain-text-index/index/INDEX_general_PL_data.2019';
data=readtable(load_path,'FileType','text');
proteinName=table2cell(data(:,1));
affinity=table2cell(data(:,4));
ligandName=table2cell(data(:,8));
T = table(proteinName,affinity,ligandName);
filename = 'PDBbind2019PLdata.csv';
writetable(T,filename);

end
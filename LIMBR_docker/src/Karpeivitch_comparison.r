source("src/EigenMS.R")

for (j in 1:20){
  
ddata = read.table(paste(c("output/simdata/mb_simulated_data_with_noise_for_sva_",toString(j),".txt"),collapse=""), header=TRUE)
ddata = ddata[,c(2,1,3:74)]
ddata[,1] <- seq.int(nrow(ddata))
m_logInts = ddata[,3:74]

m_prot.info = ddata[,1:2]

grps = as.factor(rep(1:24, times=1, each=3))
m_ints_eig1 = eig_norm1(m=m_logInts,treatment=grps,prot.info=m_prot.info)
m_ints_eig1$h.c
m_ints_norm1 = eig_norm2(rv=m_ints_eig1) 

output <- m_ints_norm1$normalized[,2:74]
newcols <- c('#')
for (i in 2:73){
  newcols[i] <- unlist(strsplit(colnames(output)[i], '_'))[1]
}
 
colnames(output) <- newcols
write.table(output,paste(c("output/simdata/mb_simdata_eigenMS_",toString(j),".txt"),collapse=""),sep='\t', quote = FALSE, row.names=FALSE)

detach(TREAT)
}
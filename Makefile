FILES = make_checkpoints/install
FILES += make_checkpoints/actual
FILES += make_checkpoints/simulate1 make_checkpoints/simulate2 make_checkpoints/simulate3 make_checkpoints/simulate4
FILES += make_checkpoints/simulate_mb1 make_checkpoints/simulate_mb2 make_checkpoints/simulate_mb3 make_checkpoints/simulate_mb4 make_checkpoints/figures make_checkpoints/figures_mb

all: ${FILES}

make_checkpoints/install : dockerbuild/Dockerfile_install
	@echo installing base image and downloading data
	@docker pull ubuntu
	@docker build --force-rm --squash -f dockerbuild/Dockerfile_install -t acrowell/limbr .
	@docker tag acrowell/limbr acrowell/limbr:1
	@touch $@

make_checkpoints/download : dockerbuild/Dockerfile_download make_checkpoints/install
	@echo downloading data
	@docker build --force-rm --squash -f dockerbuild/Dockerfile_download -t acrowell/limbr .
	@docker tag acrowell/limbr acrowell/limbr:2
	@touch $@

make_checkpoints/actual : dockerbuild/Dockerfile_actual make_checkpoints/download
	@echo running actual data
	@docker build --force-rm  --squash -f dockerbuild/Dockerfile_actual -t acrowell/limbr .    
	@docker tag acrowell/limbr acrowell/limbr:3
	@touch $@

make_checkpoints/simulate : dockerbuild/Dockerfile_sim make_checkpoints/actual
	@echo running single bias trend simulations
	@docker build --force-rm --squash -f dockerbuild/Dockerfile_sim -t acrowell/limbr .
	@docker tag acrowell/limbr acrowell/limbr:4
	@touch $@

make_checkpoints/simulate_mb : dockerbuild/Dockerfile_sim_mb make_checkpoints/simulate
	@echo running multiple bias trend simulations
	@docker build --force-rm --squash -f dockerbuild/Dockerfile_sim_mb -t acrowell/limbr .
	@docker tag acrowell/limbr acrowell/limbr:5
	@touch $@

make_checkpoints/figures : dockerbuild/Dockerfile_figs make_checkpoints/simulate_mb
	@echo making figures
	@docker build --force-rm --squash -f dockerbuild/Dockerfile_figs -t acrowell/limbr .
	@docker tag acrowell/limbr acrowell/limbr:6
	@touch $@

make_checkpoints/figures_mb : dockerbuild/Dockerfile_figs_mb make_checkpoints/figures
	@echo making figures mb
	@docker build --force-rm --squash -f dockerbuild/Dockerfile_figs_mb -t acrowell/limbr .
	@docker tag acrowell/limbr acrowell/limbr:7
	@touch $@
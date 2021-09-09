ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

test:
	docker build \
		--file ${ROOT_DIR}/Dockerfile \
		--build-arg PYTHON_VERSION=${PYTHON_VERSION} \
		--tag afdaniele/xdocker:test-${PYTHON_VERSION} \
		${ROOT_DIR}/../../ \
	&& docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock \
		afdaniele/xdocker:test-${PYTHON_VERSION} \
	&& docker rmi afdaniele/xdocker:test-${PYTHON_VERSION}

test-no-clean:
	docker build \
		--file ${ROOT_DIR}/Dockerfile \
		--build-arg PYTHON_VERSION=${PYTHON_VERSION} \
		--tag afdaniele/xdocker:test-${PYTHON_VERSION} \
		${ROOT_DIR}/../../ \
	&& docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock \
		afdaniele/xdocker:test-${PYTHON_VERSION}

test-all:
	set -e; \
	while read p; do \
	  make --file ${ROOT_DIR}/Makefile test PYTHON_VERSION=$${p}; \
	done <${ROOT_DIR}/python-versions.txt

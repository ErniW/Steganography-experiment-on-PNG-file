OPENSSL_DIR = C:/vcpkg/packages/openssl_x64-windows/include
PROJECT_NAME = test

SRCS = main.cpp

INCLUDES = $(OPENSSL_DIR)

CFLAGS = -I $(INCLUDES)

compile:
	g++ ${CFLAGS} ${SRCS} -o ./build/$(PROJECT_NAME).exe


obj = udstdExe.o

udstdExe: $(obj)
	g++ -o udstdExe $(obj)
	./udstdExe
	rm udstdExe.o

udstdExe.o:
	gcc -c udstdExe.cpp

.PHONY: clean start
clean:
	rm udstdExe
	rm *.o



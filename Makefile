hello: 
	macro11 hello90.mac -o hello90.obj
	obj2bin.pl --binary --nocrc --bytes=100000  --outfile=hello90.bin hello90.obj
	dd if=hello90.bin of=smp0.bin bs=1 skip=6
	dd if=/dev/zero of=smp0.bin bs=1 count=1 seek=10240
	rm hello90.bin

clean:
	rm hello90.obj
	rm smp0.bin


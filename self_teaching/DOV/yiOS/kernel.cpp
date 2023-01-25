#include "textprint.cpp"
#include "idt.cpp"
extern const char Test[];

extern "C" void _start() {
	clearScreen();
	setCursorPos(positionFromCoords(0, 0));
	initalizeIDT();
	return;
}
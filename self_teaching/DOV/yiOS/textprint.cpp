#pragma once
#include "IO.cpp"
#include "typedefs.cpp"
#include "textmodecolorcodes.cpp"
#define VGA_MEMORY (uint_8*)0xb8000
#define VGA_WIDTH 80
#define DEFCOLOR BG_BLACK | FG_WHITE

uint_16 CursorPosition;

void clearScreen(uint_64 clearColor = DEFCOLOR)
{
    uint_64 value = 0;
    value + clearColor << 8; // value + clearColor * 2e8
    value + clearColor << 24;
    value + clearColor << 40;
    value + clearColor << 56;
    for (uint_64* i = (uint_64*)VGA_MEMORY; i < (uint_64*)(VGA_MEMORY + 4000); i++)
    {
        *i = value;
    }
    
}


void setCursorPos(uint_16 position)
{
    outb(0x3D4, 0x0F);
    outb(0x3D5, (uint_8)(position & 0xFF));
    outb(0x3D4, 0x0E);
    outb(0x3D5, (uint_8)((position >> 8) & 0xFF));
    if(CursorPosition > 2000)
    {
        CursorPosition = 2000;
        return;
    }
    if(CursorPosition < 0)
    {
        CursorPosition = 0;
        return;
    }
    CursorPosition = position;
    return;
}

uint_16 positionFromCoords(uint_8 x, uint_8 y)
{
    return y * VGA_WIDTH + x;
}

void printString(const char* str, uint_8 color = DEFCOLOR)
{
    uint_8* charPtr = (uint_8*)str;
    uint_16 index = CursorPosition;
    while(*charPtr != 0)
    {
        switch (*charPtr)
        {
        case 10:
            index+= VGA_WIDTH;
            break;
        case 13:
            index -= index % VGA_WIDTH; //Making index a factor of VGA_WIDTH
            break;
        
        default:
            *(VGA_MEMORY + index * 2) = *charPtr;
            *(VGA_MEMORY + index * 2 + 1) = color;
            index++;
        }
        
        charPtr++;
    }
    setCursorPos(index);
}

void printChar(char chr, uint_8 color = DEFCOLOR)
{
    *(VGA_MEMORY + CursorPosition * 2) = chr;
    *(VGA_MEMORY + CursorPosition * 2 + 1) = color;
    setCursorPos(CursorPosition + 1);
}

char hexToStringOutput[128];
template<typename T>
const char* hexToString(T value)
{
    T* valPtr = &value;
    uint_8* ptr;
    uint_8 temp;
    uint_8 size = (sizeof(T)) * 2 - 1;
    uint_8 i;
    for (i=0; i < size; i++)
    {
        ptr = ((uint_8*)valPtr+i);
        temp = ((*ptr & 0xF0) >> 4);
        hexToStringOutput[size - (i * 2 + 1)] = temp + (temp > 9 ? 55 : 48);
        temp = ((*ptr & 0x0F));
        hexToStringOutput[size - (i * 2 + 0)] = temp + (temp > 9 ? 55 : 48);
    }
    hexToStringOutput[size+1]=0;
    return hexToStringOutput;
}
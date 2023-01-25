#include <iostream>
#include <card.h>

#define COUT std::cout <<

int main()
{
	try
	{
		COUT "\x1B[91mSimple Snap Card Tracker\nCopyright ComboDev - 2023\n\033[0m\t\t";
		COUT "\nThe amount of cards in Marvel Snap practically changes every week.\nIt is currently set to " + std::to_string(CardManager::amountOfCardsTotal) + ". Please update the code regularly to get appropriate statistics.";
		
		CardManager cardManager = CardManager();

		//Testing Exception
		/*for (size_t i = 0; i < 200; i++)
		{
			cardManager.addMissingCard("test", SERIES_3);
		}*/
	}
	catch (const std::exception e)
	{
		COUT "\n\n\x1B[91mEXCEPTION CATCHED:\n";
		std::cerr << e.what();
		COUT "\n\033[0m\t\t";
	}
		
	return 0;
}
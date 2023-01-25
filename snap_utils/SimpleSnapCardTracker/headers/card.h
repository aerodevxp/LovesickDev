#pragma once
#include <date.h>

enum series
{
	UNKNOWN,
	SERIES_1,
	SERIES_2,
	SERIES_3,
	SERIES_4,
	SERIES_5
};

enum quality
{
	UNKOWN,
	COMMON,
	UNCOMMON,
	RARE,
	EPIC,
	LEGENDARY,
	ULTRA,
	MAXINFINITY
};

class card
{
	public:

		card(std::string name, quality quality, series series, date dateObtained);
		card(std::string name, series series);
		card(const card&) {};
		bool cardIsOwned = false;

	private:
		std::string name;
		quality quality = UNKOWN;
		series series = UNKNOWN;
		date dateObtained = date();

};

//Obtained Card
card::card(std::string name, ::quality quality, ::series series, date dateObtained) {
	this->dateObtained.setDate(dateObtained.getDay(), dateObtained.getMonth(), dateObtained.getYear());
	this->name = name;
	this->quality = quality;
	this->series = series;
	this->cardIsOwned = true;
}

 //Missing Card
card::card(std::string name, ::series series) {
	this->name = name;
	this->series = series;
}

class CardManager
{
public:
	int amountOfCards;
	const static int amountOfCardsTotal = 198;

	void addObtainedCard(std::string name, ::quality quality, ::series series, date dateObtained);
	void addMissingCard(std::string name, ::series series);
private:
	int cardIndex = 1; //Removes a warning for some reason
	card * cards[amountOfCardsTotal];
};

void CardManager::addObtainedCard(std::string name, ::quality quality, ::series series, date dateObtained) {
	if (cardIndex > amountOfCardsTotal)
	{
		throw std::out_of_range("You've added to many cards to the card manager. Increase the card total to add more.");
	}
	card newCard = card(name, quality, series, dateObtained);
	cards[cardIndex - 1] = &newCard;
	cardIndex++;
}

void CardManager::addMissingCard(std::string name, ::series series)
{
	if (cardIndex > amountOfCardsTotal)
	{
		throw std::out_of_range("You've added too many cards to the card manager. Increase the card total to add more.");
	}
	card newCard = card(name, series);
	cards[cardIndex - 1] = &newCard;
	cardIndex++;
}
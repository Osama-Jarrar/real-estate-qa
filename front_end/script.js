// API Configuration
const API_BASE_URL = 'http://127.0.0.1:8000';
const SEARCH_ENDPOINT = '/search';

// DOM elements
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const loadingSpinner = document.getElementById('loadingSpinner');
const resultsContainer = document.getElementById('resultsContainer');
const propertyGrid = document.getElementById('propertyGrid');
const resultsCount = document.getElementById('resultsCount');
const emptyState = document.getElementById('emptyState');

// State
let currentResults = [];

// Event listeners
searchInput.addEventListener('keypress', handleKeyPress);
searchBtn.addEventListener('click', performSearch);
searchInput.addEventListener('input', handleInputChange);

function handleKeyPress(e) {
    if (e.key === 'Enter') {
        performSearch();
    }
}

function handleInputChange() {
    if (searchInput.value.trim() === '') {
        showEmptyState();
    }
}

function performSearch() {
    const query = searchInput.value.trim();
    
    if (!query) {
        showEmptyState();
        return;
    }

    showLoading();
    
    // Call your FastAPI backend
    searchProperties(query)
        .then(results => {
            displayResults(results, query);
        })
        .catch(error => {
            console.error('Search failed:', error);
            showError('Unable to search properties. Please try again.');
        });
}

async function searchProperties(query) {
    try {
        const response = await fetch(`${API_BASE_URL}${SEARCH_ENDPOINT}?query=${encodeURIComponent(query)}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Check if the response contains an error
        if (data.error) {
            throw new Error(data.error);
        }
        
        // Transform the data if needed - adjust this based on your RAG pipeline output format
        return Array.isArray(data) ? data : (data.results || []);
        
    } catch (error) {
        console.error('API call failed:', error);
        throw error;
    }
}

function displayResults(results, query) {
    currentResults = results;
    hideLoading();
    
    if (results.length === 0) {
        showNoResults(query);
        return;
    }
    
    showResults();
    updateResultsCount(results.length);
    renderPropertyCards(results);
}

function renderPropertyCards(properties) {
    propertyGrid.innerHTML = '';
    
    properties.forEach(property => {
        const card = createPropertyCard(property);
        propertyGrid.appendChild(card);
    });
}

function createPropertyCard(property) {
    const card = document.createElement('div');
    card.className = 'property-card';
    card.onclick = () => handlePropertyClick(property);
    
    // Format price
    const price = property.price ? `${property.price.toLocaleString()}` : 'Price not available';
    
    // Format bedrooms
    const bedrooms = property.bedrooms || 0;
    const bedroomText = bedrooms === 0 ? 'Studio' : 
                      bedrooms === 1 ? '1 bedroom' : 
                      `${bedrooms} bedrooms`;
    
    // Format bathrooms (handle decimal bathrooms like 1.75)
    const bathrooms = property.bathrooms || 0;
    const bathroomText = bathrooms === 1 ? '1 bath' : `${bathrooms} baths`;
    
    // Format square footage
    const sqft = property.sqft_living || property.sqft_above || 0;
    const sqftText = sqft ? `${sqft.toLocaleString()} sq ft` : '';
    
    // Create location from zipcode and coordinates if available
    const location = property.zipcode ? `ZIP ${property.zipcode}` : 
                    (property.lat && property.long) ? `${property.lat.toFixed(3)}, ${property.long.toFixed(3)}` : '';
    
    // Generate a title based on property characteristics
    const title = generatePropertyTitle(property);
    
    // Get year built info
    const yearBuilt = property.yr_built ? `Built ${property.yr_built}` : '';
    
    // Get condition info
    const condition = property.condition || '';
    
    card.innerHTML = `
        <div class="property-image placeholder">
            <span>Property Image</span>
            ${property.score ? `<div class="match-score">Match: ${Math.round(property.score * 100)}%</div>` : ''}
        </div>
        <div class="property-details">
            <h3 class="property-title">${title}</h3>
            <div class="property-price">${price}</div>
            <div class="property-features">
                <div class="feature">🏠 ${bedroomText}</div>
                <div class="feature">🚿 ${bathroomText}</div>
                ${sqft ? `<div class="feature">📐 ${sqftText}</div>` : ''}
                ${location ? `<div class="feature">📍 ${location}</div>` : ''}
                ${yearBuilt ? `<div class="feature">📅 ${yearBuilt}</div>` : ''}
                ${condition ? `<div class="feature">⭐ ${condition}</div>` : ''}
            </div>
            ${property.description ? `<div class="property-description">${truncateDescription(property.description)}</div>` : ''}
        </div>
    `;
    
    return card;
}

function generatePropertyTitle(property) {
    const bedrooms = property.bedrooms || 0;
    const price = property.price || 0;
    const waterfront = property.waterfront;
    const grade = property.grade || '';
    const floors = property.floors || 1;
    
    // Create descriptive title based on property features
    let title = '';
    
    if (waterfront) {
        title = 'Waterfront ';
    } else if (grade.toLowerCase().includes('luxury') || price > 1000000) {
        title = 'Luxury ';
    } else if (grade.toLowerCase().includes('above average')) {
        title = 'Premium ';
    }
    
    if (bedrooms === 0) {
        title += 'Studio';
    } else if (bedrooms >= 4) {
        title += 'Spacious Family Home';
    } else if (bedrooms === 1) {
        title += 'Cozy 1-Bedroom';
    } else {
        title += `${bedrooms}-Bedroom Home`;
    }
    
    if (floors > 1) {
        title += ` (${floors} floors)`;
    }
    
    return title || 'Residential Property';
}

function truncateDescription(description, maxLength = 120) {
    if (!description) return '';
    if (description.length <= maxLength) return description;
    return description.substring(0, maxLength).trim() + '...';
}

function handlePropertyClick(property) {
    // Create a detailed view of the property
    const details = Object.entries(property)
        .filter(([key, value]) => value !== null && value !== undefined && value !== '')
        .map(([key, value]) => `${key}: ${value}`)
        .join('\n');
    
    alert(`Property Details:\n\n${details}`);
}

function showError(message) {
    hideLoading();
    emptyState.innerHTML = `
        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="8" x2="12" y2="12"></line>
            <line x1="12" y1="16" x2="12.01" y2="16"></line>
        </svg>
        <h3>Search Error</h3>
        <p>${message}</p>
        <button onclick="showEmptyState()" style="
            margin-top: 20px;
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        ">Try Again</button>
    `;
    emptyState.classList.remove('hidden');
    resultsContainer.classList.add('hidden');
}

function showLoading() {
    emptyState.classList.add('hidden');
    resultsContainer.classList.add('hidden');
    loadingSpinner.classList.remove('hidden');
}

function hideLoading() {
    loadingSpinner.classList.add('hidden');
}

function showResults() {
    emptyState.classList.add('hidden');
    resultsContainer.classList.remove('hidden');
}

function showEmptyState() {
    loadingSpinner.classList.add('hidden');
    resultsContainer.classList.add('hidden');
    emptyState.classList.remove('hidden');
}

function showNoResults(query) {
    emptyState.innerHTML = `
        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.35-4.35"></path>
        </svg>
        <h3>No properties found</h3>
        <p>We couldn't find any properties matching "${query}". Try searching with different keywords.</p>
    `;
    emptyState.classList.remove('hidden');
    resultsContainer.classList.add('hidden');
}

function updateResultsCount(count) {
    const propertyText = count === 1 ? 'property' : 'properties';
    resultsCount.textContent = `${count} ${propertyText} found`;
}

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
    showEmptyState();
    searchInput.focus();
});
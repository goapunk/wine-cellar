import React from 'react'
import django from 'django'
import {
  MapPopup
} from './MapPopup'

const translations = {
  getComments: (count) => {
    const countText = django.ngettext('Comment', 'Comments', count)
    return django.interpolate(countText, [count])
  },
  getLikes: (count) => {
    const countText = django.ngettext('Like', 'Likes', count)
    return django.interpolate(countText, [count])
  },
  getDislikes: (count) => {
    const countText = django.ngettext('Dislike', 'Dislikes', count)
    return django.interpolate(countText, [count])
  },
  support: django.gettext('Support'),
  detailsStr: django.gettext('Show'),
  toStr: django.gettext('to:')
}

/**
 * Renders a popup for an item feature on a map.
 *
 * @param {Object} props - The component props.
 * @param {Object} props.feature - The geojson feature.
 * @returns {JSX.Element} The JSX element representing the popup.
 */
export const ItemPopup = ({ feature }) => {
  return (
    <MapPopup feature={feature}>
      <div className="maps-popups-popup-name">
        <a href={feature.properties.url}>
          {feature.properties.name}
        </a>
      </div>
      <div className="maps-popups-popup-meta">
      </div>
      <a href={feature.properties.url} className="more">{translations.detailsStr}
        <span className="aural">{translations.toStr} {feature.properties.name}</span>
      </a>
    </MapPopup>
  )
}
